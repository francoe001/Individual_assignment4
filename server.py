#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 26 15:22:35 2018

@author: efrancois
"""
#%%
#1.Create a route in the server to which the user can upload a graph using
#JSON and using the POST http method. The JSON data should be
#passed as part of the request body, not in the URL.

from flask import Flask, jsonify, request

server = Flask("graph server")

@server.route('/upload_graph', methods=['POST'])
def upload_graph():
    body = request.get_json()
    return jsonify(body)


@server.route("degrees_of_separation/<origin>/<destination>", methods=['PUT'])
def degrees_of_separation(origin,destination,graph="",path=[]):
    
    graph=request.get_json()
    
    path=path+[origin]
    
    if origin==destination:
        degree=len(path) - 2
        
        if degree==0:
            return jsonify("nodes are connected")
        
        else:
            return jsonify(degree)
        
    if origin not in graph:
        return jsonify(None)
    
    for connection in graph[origin]:
        if connection not in path:
            newpath=degrees_of_separation(connection, destination, graph, path)
            if newpath is not None:
                return newpath
            
    return jsonify(None)

server.run()

