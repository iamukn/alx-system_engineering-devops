# A puppet manuscript that replaces a line in a file on a server

$file_to_modify = '/var/www/html/wp-settings.php'

#replace phrase containing "phpp" with "php"

exec { 'replace_line':
  command => "sed -i 's/phpp/php/g' ${file_to_modify}",
  path    => ['/bin','/usr/bin']
}
