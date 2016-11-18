#!/bin/bash
g++ messages.cpp -o messages `mysql_config --cxxflags --libs`
