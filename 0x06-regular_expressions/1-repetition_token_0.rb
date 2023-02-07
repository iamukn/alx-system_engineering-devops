#/usr/bin/env ruby
# Regex to match a repititive character
puts ARGV[0].scan(/hbt{2,5}n/).join
