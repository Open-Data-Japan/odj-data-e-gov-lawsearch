#!/bin/bash

curl "https://elaws.e-gov.go.jp/download?file_section=1&only_xml_flag=true" -A "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0" --output all_xml.zip
unzip all_xml.zip -d all_xml
