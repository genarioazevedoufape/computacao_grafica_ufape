def main():
    filename = input('Arquivo OFF: ')
    linhas = ""

    with open(filename + '.off', 'r') as f:
        linhas = f.read()

    linhas = linhas.split('\n')
    
    del linhas[0]

    num_v_f = linhas[0].split()
    del linhas[0]

    num_v = num_v_f[0]
    num_f = num_v_f[1]  

    vertices = [linhas.pop(0) for x in range(int(num_v))]

    faces = [linhas.pop(0) for x in range(int(num_f))]   

    verticesTable = ""
    facesTable = ""
    facesVT = ''

    for x in range(len(vertices)):
        for j in range(len(faces)):
            aux = faces[j].split(' ')
            aux.pop(0)
            if str(x) in aux:
                if not facesVT:
                    facesVT += "['F" + str(j) + "'"
                else:
                    facesVT += ", 'F" + str(j) + "'"
        if facesVT:
            facesVT += ']'
            verticesTable += f"('V{x}:',[{vertices[x]}], {facesVT})\n"
        else:
            verticesTable += f"('V{x}:',[{vertices[x]}])\n"
        facesVT = ''

    faceVT = ''
    for i, face in enumerate(faces):
        faceSplit = face.split(' ')[1:]
        aux = []
        for vertexIndex in faceSplit:
            aux.append('V' + vertexIndex)
        faceVT = ", ".join(aux)
        facesTable += f"('F{i}', ['{faceVT}'])\n"
        faceVT = ''

    print('\nTABELA DE VERTICES')
    print(verticesTable)

    print('TABELA DE FACES')
    print(facesTable)

if __name__ == '__main__':
    main()
