#!/usr/bin/env ruby
#
str = "School"
ARGV.each do |arg|
  if ARGV[1].nil?
    puts ARGV[0].scan(str).join
  end
end
