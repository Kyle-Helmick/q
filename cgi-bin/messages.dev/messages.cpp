// messages.cpp -- Expeimental (relatively) high-performance C++ implementation
// of the most commonly accessed API.
// Created by Michael Gohde some time in mid-November.

#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <vector>
#include <string>

#include <my_global.h>
#include <mysql.h>

char **splitpath(char *src, int *numtoks)
{
	char *tmp;
	char *newstr;
	char **retarr;
	std::vector<char*> retlist;
	int numelems, i;
	
	newstr=strdup(src);
	
    tmp=strtok(newstr, "/");
	
	do
	{
        retlist.push_back(strdup(tmp));
	} while((tmp=strtok(NULL, "/"))!=NULL);

    free(newstr);
	
	numelems=retlist.size();
	(*numtoks)=numelems;
	retarr=(char**) malloc(sizeof(char*)*numelems);
	
	for(i=0;i<numelems;i++)
	{
		retarr[i]=retlist[i];
	}
	
	return retarr;
}

char *urlsanitize(char *url)
{
	int i, len;
	int charval;
	std::vector<char> newStr;
	char *retstr;
	
	len=strlen(url);
	
	for(i=0;i<len;i++)
	{
		if(url[i]=='%')
		{
			sscanf(url+i+1, "%x", &charval);
			newStr.push_back((char) charval);
			i+=2;
		}
		
		else
		{
			newStr.push_back(url[i]);
		}
	}
	
	retstr=(char*) malloc(sizeof(char)*newStr.size()+1);
	len=newStr.size();
	
	for(i=0;i<len;i++)
	{
		retstr[i]=newStr[i];
	}
	
	retstr[len]='\0';
	
	return retstr;
}

char *replace(char *src, char oldc, char newc)
{
	char *retstr;
	int i;
	int len;
	
	retstr=strdup(src);
	len=strlen(retstr);
	
	for(i=0;i<len;i++)
	{
		if(retstr[i]==oldc)
		{
			retstr[i]=newc;
		}
	}
	
	return retstr;
}

void gen400()
{
    printf("Status: 400\n\n");
}

void gen500()
{
    printf("Status: 500\n\n");
}

void printHeader()
{
    printf("Content-type: application/json\n\n");
}

char *getUserId(MYSQL *con, char *sessionid)
{
	char *retVal;
	char *buf;
	MYSQL_RES *reslt;
	MYSQL_ROW r;
	
	buf=(char*) malloc(sizeof(char)*(strlen(sessionid)+255));
	sprintf(buf, "SELECT userid FROM sessions WHERE sessionid='%s'", sessionid);
	
	if(mysql_query(con, buf))
	{
		gen400();
		free(buf);
		exit(-1);
	}
	
	free(buf);
	reslt=mysql_store_result(con);
	
	if(reslt==NULL)
	{
		gen400();
		mysql_close(con);
		exit(-1);
	}
	
	r=mysql_fetch_row(reslt);
	
	if(!r)
	{
		mysql_free_result(reslt);
		mysql_close(con);
		exit(-1);
	}
	
	retVal=strdup(r[0]);
	mysql_free_result(reslt);
	
	return retVal;
}

void getMessage(MYSQL *con, char *sessionid, char *messageid)
{
    char *userid;
    char *buf;
    MYSQL_RES *reslt;
    MYSQL_ROW r;
    int i;

    userid=getUserId(con, sessionid);
    buf=(char*) malloc(sizeof(char)*(strlen(sessionid)+strlen(messageid)+255));

    sprintf(buf, "SELECT * FROM usrentries WHERE userid=%s AND entryid=%s", userid, messageid);

    if(mysql_query(con, buf))
    {
        gen400();
        free(buf);
        mysql_close(con);
        exit(-1);
    }

    free(buf);

    reslt=mysql_store_result(con);

    printHeader();

    printf("{");
    if(!(r=mysql_fetch_row(reslt)))
    {
        gen400();
        printf("}");
        return;
    }

    //Sorry for the absurdly long line!
    printf("\"entryid\": \"%s\", \"userid\": \"%s\", \"text\": \"%s\", \"class\": \"%s\", \"duedate\": \"%s\", \"priority\": \"%s\", \"title\": \"%s\"}",
           r[0], r[1], r[2], r[3], r[4], r[5], r[6]);

    mysql_free_result(reslt);
    free(userid);
}

void listMessages(MYSQL *con, char *sessionid)
{
    char *userid;
    char *buf;
    MYSQL_RES *reslt;
    MYSQL_ROW r;
    std::vector<MYSQL_ROW> rows;
    int i;
    int numrows;
	
    userid=getUserId(con, sessionid);
    buf=(char*) malloc(sizeof(char)*(strlen(sessionid)+255));
	
    sprintf(buf, "SELECT entryid, title FROM usrentries WHERE userid=%s", userid);
	
    if(mysql_query(con, buf))
    {
        gen400();
        free(buf);
        mysql_close(con);
        exit(-1);
    }
	
    free(buf);
	
    reslt=mysql_store_result(con);
    printHeader();
    printf("{");
	
    while((r=mysql_fetch_row(reslt)))
	{
        rows.push_back(r);
        //printf("\"%s\": \"%s\",", r[0], r[1]);
    }
	
    numrows=rows.size();
	
    if(numrows>0)
    {
        numrows--;
        for(i=0;i<numrows;i++)
        {
            r=rows[i];
            printf("\"%s\": \"%s\",", r[0], r[1]);
        }
	
        r=rows[numrows];
        printf("\"%s\": \"%s\"", r[0], r[1]);
        printf("}");
    }
    
    else
    {
        printf("{}");
    }
	
	mysql_free_result(reslt);
	
	free(userid);
}

void newMessage(MYSQL *con, char *sessionid, char *priority, char *content, char *cls, char *duedate, char *title)
{
    char *buf;
    char *userid;
    int totallen=0;
    int id;

    userid=getUserId(con, sessionid);
    totallen=strlen(priority)+strlen(content)+strlen(cls)+strlen(duedate)+strlen(title);
    buf=(char*) malloc(sizeof(char*)*(totallen+255));

    sprintf(buf, "INSERT INTO usrentries (userid, description, class, duedate, priority, title) VALUES (%s, '%s', '%s', '%s', '%s', '%s')",
            userid, content, cls, duedate, priority, title);

    if(mysql_query(con, buf))
    {
        gen400();
        free(buf);
        free(userid);
        mysql_close(con);
        exit(-1);
    }

    id=mysql_insert_id(con);

    printf("{\"entryid\":\"%d\"", id);

    free(buf);
    free(userid);
}

void freepathtoks(char ***pathtoks, int numtoks)
{
	char **toks;
	int i;
	
    toks=(*pathtoks);

    for(i=0;i<numtoks;i++)
    {
        free(toks[i]);
    }
	
	free(toks);
	(*pathtoks)=NULL;
}

int main(int argc, char **argv, char **envp)
{
	char *reqmethod;
	char *rsrc;
	char *query;
	char **pathtoks;
	char *tmp;
	int numpathtoks;
	MYSQL *con;
	
	
	reqmethod=getenv("REQUEST_METHOD");
	
	rsrc=replace(getenv("PATH_INFO"), '+', ' ');
	tmp=urlsanitize(rsrc);
	free(rsrc);
	rsrc=tmp;
	
	query=getenv("QUERY_STRING");
	
	con=mysql_init(NULL);
	if(mysql_real_connect(con, "localhost", "hashteam", "passw0rd", "qdata", 0, NULL, 0)==NULL)
    {
        gen500();
        return 0;
    }
	
	pathtoks=splitpath(rsrc, &numpathtoks);
	
	if(!strcmp(reqmethod, "GET"))
	{
		if(numpathtoks==2)
		{
			if(strcmp(pathtoks[1], "list")==0)
			{
				listMessages(con, pathtoks[0]);
			}

            else
            {
                getMessage(con, pathtoks[0], pathtoks[1]);
            }
		}
	}

    else if(!strcmp(reqmethod, "PUT") && numpathtoks==6)
    {
        newMessage(con, pathtoks[0], pathtoks[1], pathtoks[2], pathtoks[3], pathtoks[4], pathtoks[5]);
    }
	
	else
	{
		gen400();
	}
	
    mysql_close(con);
	//TODO: Find out what the hell is going on with this function:
    freepathtoks(&pathtoks, numpathtoks);
	return 0;
}
