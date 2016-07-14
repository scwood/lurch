module Seize
  module Utils
    def self.truncate(string, length)
      if string.nil?
        'None'
      elsif string.length <= length
        string
      else
        string[0..length-3] + '...'
      end
    end

    def self.commaize(number)
      number.to_s.reverse.split('').each_slice(3).map(&:join).join(',').reverse
    end
  end
end
