import os, shutil, csv, argparse

os.getcwd()
os.chdir('C:\\Users\\rehra\\Desktop\\FileOrganizer\\files')

#Crea file recap.csv in modalità append
recap = open('recap.csv', 'a', newline='')
writer = csv.writer(recap)

#Controlla se necessario scrivere l'heading del file recap.csv
file_is_empty = os.stat('recap.csv').st_size == 0
if file_is_empty:
    writer.writerow(('name', 'type', 'size(B)'))

#Permette di passare il valore dal terminale
parser = argparse.ArgumentParser(description='Gli viene passato un file e lo sposta nella cartella adeguata')
parser.add_argument('x', help='File da passare')
args = parser.parse_args()

file_name_split = args.x.split('.')
est = file_name_split[-1]

if est == 'mp3':
    type_name = 'audio'
    # Verifica la presenza della cartella 'audio', se non presente la crea
    if 'audio' not in os.listdir():
        os.makedirs('C:\\Users\\rehra\\Desktop\\FileOrganizer\\files\\audio')
    # Sposta il file nella cartella
    shutil.move(f'C:\\Users\\rehra\\Desktop\\FileOrganizer\\files\\{args.x}', f'C:\\Users\\rehra\\Desktop\\FileOrganizer\\files\\audio\\{args.x}')
    # Ottiene le dimensioni in Byte del file
    size = os.stat(f'C:\\Users\\rehra\\Desktop\\FileOrganizer\\files\\audio\\{args.x}').st_size
    print(f'{file_name_split[0]} type:{type_name} size:{size}B')
    # Inserisce i valori nel file recap.csv
    tup = (args.x, type_name, size)
    writer.writerow(tup)
elif est == 'txt' or est == 'odt':
    type_name = 'doc'
    # Verifica la presenza della cartella 'audio', se non presente la crea
    if 'docs' not in os.listdir():
        os.makedirs('C:\\Users\\rehra\\Desktop\\FileOrganizer\\files\\docs')
    # Sposta il file nella cartella
    shutil.move(f'C:\\Users\\rehra\\Desktop\\FileOrganizer\\files\\{args.x}', f'C:\\Users\\rehra\\Desktop\\FileOrganizer\\files\\docs\\{args.x}')
    # Ottiene le dimensioni in Byte del file
    size = os.stat(f'C:\\Users\\rehra\\Desktop\\FileOrganizer\\files\\docs\\{args.x}').st_size
    print(f'{file_name_split[0]} type:{type_name} size:{size}B')
    # Inserisce i valori nel file recap.csv
    tup = (args.x, type_name, size)
    writer.writerow(tup)
elif est == 'png' or est == 'jpg' or est == 'jpeg':
    type_name = 'image'
    # Verifica la presenza della cartella 'audio', se non presente la crea
    if 'images' not in os.listdir():
        os.makedirs('C:\\Users\\rehra\\Desktop\\FileOrganizer\\files\\images')
        # Sposta il file nella cartella
    shutil.move(f'C:\\Users\\rehra\\Desktop\\FileOrganizer\\files\\{args.x}', f'C:\\Users\\rehra\\Desktop\\FileOrganizer\\files\\images\\{args.x}')
    # Ottiene le dimensioni in Byte del file
    size = os.stat(f'C:\\Users\\rehra\\Desktop\\FileOrganizer\\files\\images\\{args.x}').st_size
    print(f'{file_name_split[0]} type:{type_name} size:{size}B')
    # Inserisce i valori nel file recap.csv
    tup = (args.x, type_name, size)
    writer.writerow(tup)
else:
    #Risposta se file inserito errato
    estensioni = ['png', 'txt', 'jpg', 'odt', 'mp3', 'jpeg']
    file = [x for x in os.listdir() if len(x.split('.')) == 2 and  x.split('.')[1] in estensioni]
    print(f'Il file inserito è errato inserisci un file tra {file}')
recap.close()