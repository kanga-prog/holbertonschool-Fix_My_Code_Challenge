#!/usr/bin/env ruby

# Récupère les arguments numériques depuis ARGV
numbers = ARGV.select { |arg| arg.match?(/^[-+]?\d+$/) }.map(&:to_i)

# Tri en ordre croissant (et non décroissant)
sorted = numbers.sort

# Affichage ligne par ligne
sorted.each { |n| puts n }
