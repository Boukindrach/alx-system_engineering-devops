#Install flask / Version must be 2.1.0

package { ['Flask', 'Werkzeug']:
  ensure   => '2.1.0',
  provider => 'pip3',
}
