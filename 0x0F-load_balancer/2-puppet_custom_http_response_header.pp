#!/usr/bin/env bash

exec { 'update':
  command  => 'sudo apt-get update',
  path     => '/usr/bin:/usr/sbin:/bin',
}

exec { 'install nginx':
  command  => 'sudo apt-get install -y nginx',
  path     => '/usr/bin:/usr/sbin:/bin',
}

file_line { 'write content':
  ensure   => present,
  path     => '/etc/nginx/sites-available/default',
  line     => "\tadd_header X-Served-By ${hostname};",
  after    => 'server_name _;',
}

file { '/var/www/html/index.nginx-debian.html':
 ensure    => present,
 content   => "Hello world!",
}

file { '/var/www/html/404.html':
 ensure    =>present,
 content   => "Ceci n'est pas une page",
}

file_line { 'write redirect':
  ensure   => present,
  path     => '/etc/nginx/sites-available/default',
  line     => "rewrite ^\/redirect_me https:\/\/github.com\/Pumelela-Banca permanent;",
  after    => 'server_name _;',
}

file_line { 'write redirect 404':
  ensure   => present,
  path     => '/etc/nginx/sites-available/default',
  line     => "\n\terror_page 404 \/404.html;\n\tlocation = \/404.html {\n\t\troot \/var\/www\/html;\n\t}",
  after    => 'listen 80 default_server;',
}

servirce { 'nginx':
  ensure => running,
}
