#!/usr/bin/env ruby
#
str = "School"
ARGV.each do |arg|
  if ARGV[1].nil?
    puts ARGV[0].scan(/hbt{2,5}n/).join
  end
end
