# allow user holberton to access files

exec { 'increase file limit':
  command => '/holberton hard/s/5/50000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/',
}
