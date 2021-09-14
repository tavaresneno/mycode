#!/usr/bin/env python3
import json # working with JSON data
import random

def main():
    with open("trivia.json", "r") as jsonfile:
        fog = json.load(jsonfile)
        for instances in fog:
            print("Here is the question:", instances['question'])
            ansc = instances['correct_answer']
            ansi = instances['incorrect_answers']
            ansprint = (ansc, ansi)
            print("Here is the answers:", random.choice(ansprint))
            #print("Here is the answers:", instances['incorrect_answers'])
main()
