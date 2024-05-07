#!/usr/bin/env ruby
#

ARGV.each do |arg|
  if ARGV[1].nil?
    puts ARGV[0].scan(/^\d{10,10}$/).join
  end
end
