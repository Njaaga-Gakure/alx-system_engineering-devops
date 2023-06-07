# Fix typo in extension

exec { 'correct_typo':
  command => "sed -i 's/phpp/php/g' '/var/www/html/wp-settings.php'",
  path    => ['/bin','/usr/bin']
}
