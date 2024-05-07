#!/usr/bin/env ruby
#

ARGV.each do |arg|
  if ARGV[1].nil?
    puts ARGV[0].scan(/[A-Z]*/).join
  end
end
