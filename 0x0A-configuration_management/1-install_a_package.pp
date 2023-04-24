# install flask in Puppet
# ensure its version is 2.1.0


exec {'install flask':
  command => '/usr/bin/pip3 install Flask==2.1.0',
  unless  => '/usr/bin/pip show Flask | /bin/grep -q "Version: 2.1.0"',
}

