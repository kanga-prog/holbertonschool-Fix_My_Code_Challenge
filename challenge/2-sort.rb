#!/usr/bin/env ruby

# Récupère les arguments de la ligne de commande
args = ARGV

# Filtrer uniquement les arguments numériques valides
numbers = args.select { |arg| arg.match?(/^[-+]?\d+$/) }.map(&:to_i)

# Trier en ordre décroissant
sorted = numbers.sort.reverse

# Afficher chaque nombre
sorted.each { |n| puts n }
