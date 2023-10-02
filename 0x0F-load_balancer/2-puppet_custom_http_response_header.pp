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

servirce { 'nginx':
  ensure => running,
}
