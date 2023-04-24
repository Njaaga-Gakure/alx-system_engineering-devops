# create a file
# path of the file is /tmp/school
# give all permissions to owner
# give read permission to group
# give read permissions to others
# set the owner of the group to be www-data

file {'/tmp/school':
  ensure  => present,
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data',
  content => 'I love Puppet'
}
