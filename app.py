bam = input('insira sua bam: ')
tarefa = input('Insira sua tarefa: ')
tarefaParser = tarefa.lower().replace(
    " ", "-").replace("ç", "c").replace("ã", "a").replace("é", "e")
print('{}/{}'.format(bam, tarefaParser))
