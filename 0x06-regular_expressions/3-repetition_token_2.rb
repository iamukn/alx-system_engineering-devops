#!/usr/bin/env ruby
# A regex that matches hbtn, hbttn,hbtttn,hbttttn
puts ARGV[0].scan(/hbt{1,}n/).join
