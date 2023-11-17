# allow user holberton to access files

exec { 'increase file limit':
  command => 'sed -i "/holberton hard/s/5/50000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/',
}

exec { 'increase file soft limit':
  command => 'sed -i  "/holberton soft/s/4/50000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/',
}
