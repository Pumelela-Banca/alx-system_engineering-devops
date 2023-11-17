# increasing traffic

exec { 'increase traffic':
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin',
}

exec { 'start nginx':
  command => 'nginx restart',
  path    => '/etc/init.d',
}
