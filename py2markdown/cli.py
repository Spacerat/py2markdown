#!/usr/bin/env python3

import py2markdown

import click


@click.command()
@click.argument("src", type=click.File("r"))
def main(src):
    print(py2markdown.process_source(src.read()))
