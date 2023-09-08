How can I create, copy, and delete files and directories?
How can I edit files?

## Buenas prácticas

- Ocupar nombres sin espacio en los directorios
- Evitar nombres de directorios que empiecen con -
- Ocupar siempre los mismo carácteres (., - o _)

## Para crear/editar archivos, se ocupa nano (que es como el block de notas, pero de Linux)

```
nano filename.txt
```

## Para mover/copiar un archivo se ocupa mv o cp, respectivamente.

```
mv archivo_a_mover directorio_destino
cp archivo_a_copiar directorio_destino
```

## Con mv se puede renombrar un archivo.
```
mv texsdto.txt texto.txt
```

## Con rm se puede quitar un archivo.

# Cheat Sheet

cp [old] [new] copies a file.

mkdir [path] creates a new directory.

mv [old] [new] moves (renames) a file or directory.

rm [path] removes (deletes) a file.

* matches zero or more characters in a filename, so *.txt matches all files ending in .txt.

? matches any single character in a filename, so ?.txt matches a.txt but not any.txt.

Use of the Control key may be described in many ways, including Ctrl-X, Control-X, and ^X.

The shell does not have a trash bin: once something is deleted, it’s really gone.

Most files’ names are something.extension. The extension isn’t required, and doesn’t guarantee anything, but is normally used to indicate the type of data in the file.

Depending on the type of work you do, you may need a more powerful text editor than Nano.