# kill a process using puppet

exec {'kill process':
  command => '/usr/bin/pkill killmenow',
}
