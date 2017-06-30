#!/usr/bin/env python3
# coding: utf-8

import xml.etree.ElementTree as ET

import mars.app.word


def convert(page=0, size=0):
    words = mars.app.word.get_words(page=page, size=size)
    for word in words:
        tree = ET.ElementTree(ET.fromstring(word['Defi'].encode('utf-8')))
        root = tree.getroot()
        sentences = [{'cn': e.find("./S/D").text, 'en': e.find("./T/D").text} for e in root.findall("./SENT/ST/SENT_P")]
        mars.app.word.update_word(word['id'], sentences=str(sentences))


if __name__ == '__main__':
    convert()
