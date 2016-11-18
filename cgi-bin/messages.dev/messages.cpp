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
	
	tmp=strtok(src, "/");
	
	do
	{
		retlist.push_back(tmp);
	} while((tmp=strtok(NULL, "/"))!=NULL);
	
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
	
	numrows=rows.size()-1;
	
	for(i=0;i<numrows;i++)
	{
	    printf("\"%s\": \"%s\",", rows[i][0], r[i][1]);
	}
	
    printf("\"%s\": \"%s\"", rows[numrows+1][0], r[i][1]);
	printf("}");
	
	mysql_free_result(reslt);
	
	free(userid);
}

void freepathtoks(char ***pathtoks, int numtoks)
{
	char **toks;
	int i;
	
	toks=(*pathtoks);
	
	for(i=0;i<numtoks;i++)
	{
		printf("Freeing %d\n", i);
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
			
		}
	}
	
	else
	{
		gen400();
	}
	
	mysql_close(con);
	//TODO: Find out what the hell is going on with this function:
	//freepathtoks(&pathtoks, numpathtoks);
	free(rsrc);
	return 0;
}
