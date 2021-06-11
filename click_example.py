#!/usr/bin/env python

import click

@click.command()
@click.option('--host', prompt='Host IP', default='0.0.0.0', help='Host IP address')
@click.option('--port', prompt='Host port', default=80, help='Host port')

def main(host, port):
    """This is a test """
    click.echo('Host: '+host+' Port: '+str(port))

if __name__ == '__main__':
    print("Hello World")
    main()
