#!/usr/bin/env python

import os
import pypandoc

source_dir = 'docs/carpeta1'
result_dir = 'docs/results_html'


for file in os.listdir(source_dir):

    source_file = source_dir+'/'+file
    output_file = result_dir+'/'+file.replace('.md','.html')
    pypandoc.convert_file(source_file,'html',outputfile=output_file)
    print source_file
    print output_file
   


