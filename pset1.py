# IDENTIFICAÇÃO DO ESTUDANTE:
# Preencha seus dados e leia a declaração de honestidade abaixo. NÃO APAGUE
# nenhuma linha deste comentário de seu código!
#
#    Nome completo: Bruno Santos Lokchin
#    Matrícula: 202200639
#    Turma: CC3M
#    Email: brunosl733@gmail.com
#
# DECLARAÇÃO DE HONESTIDADE ACADÊMICA:
# Eu afirmo que o código abaixo foi de minha autoria. Também afirmo que não
# pratiquei nenhuma forma de "cola" ou "plágio" na elaboração do programa,
# e que não violei nenhuma das normas de integridade acadêmica da disciplina.
# Estou ciente de que todo código enviado será verificado automaticamente
# contra plágio e que caso eu tenha praticado qualquer atividade proibida
# conforme as normas da disciplina, estou sujeito à penalidades conforme
# definidas pelo professor da disciplina e/ou instituição.
#


# Imports permitidos (não utilize nenhum outro import!):
import sys
import math
import base64
import tkinter
from io import BytesIO
from PIL import Image as PILImage

# Classe Imagem:
class Imagem:
    def __init__(self, largura, altura, pixels):
        self.largura = largura
        self.altura = altura
        self.pixels = pixels

    # Getter e setter
    def get_pixel(self, x, y):
        return self.pixels[y * self.largura + x] # Corrigido erro de listas se tornando tuplas
    
    # Função que extende os limites de pixel na borda
    def get_pixel_borda(self, x, y):
        if x > self.largura - 1:
            x = self.largura - 1
        elif x < 0:
            x = 0
        if y > self.altura - 1:
            y = self.altura - 1
        elif y < 0:
            y = 0
        return self.get_pixel(x, y)

    def set_pixel(self, x, y, c):
        self.pixels[y * self.largura + x] = c

   # Método para aplicar por cor, no caso, pixel
    def aplicar_por_pixel(self, func):
        resultado = Imagem.nova(self.largura, self.altura)
        """
        Não havia um for matricial correto
        X = "", e Y= "" estavam implementados de forma errada
        """
        for x in range(self.largura):
            for y in range(self.altura):
                cor = self.get_pixel(x, y)
                novo_pixel = func(cor)
                resultado.set_pixel(x, y, novo_pixel) # X e Y trocados
        return resultado

    def invertida(self, c=None):
        return self.aplicar_por_pixel(lambda c: 255 - c) #Corrigido de 256
    
    # Método para correlação de imagem com um kernel
    def correlacionar(self, kernel):
        resultado = Imagem.nova(self.largura, self.altura)
        tamanho_kernel = len(kernel) // 2
        for x in range(resultado.largura):
            for y in range(resultado.altura):
                soma = 0.0
                for i in range(len(kernel)):
                    for j in range(len(kernel[i])):
                        pixel_x = x - tamanho_kernel + j
                        pixel_y = y - tamanho_kernel + i
                        soma += self.get_pixel_borda(pixel_x, pixel_y) * kernel[i][j]
                resultado.set_pixel(x, y, soma)
        return resultado

    def borrada(self, n):
        kernel_valor = 1 / (n * n) # Valor dos elementos do kernel
        kernel = [[kernel_valor] * n for _ in range(n)] # Cria a matriz do kernel que será usado para borrar
        resultado = self.correlacionar(kernel) # Correlaciona com o kernel utilizado
        # O código abaixo serve para controlar o brilho entre 0-255 
        resultado = resultado.aplicar_por_pixel(lambda c: max(min(round(c), 255), 0))
        return resultado

    def focada(self, n):
        resultado = Imagem.nova(self.largura, self.altura)
        borrada = self.borrada(n)  # Aplica o efeito de borramento usando o método "borrada"
        for x in range(self.largura):
            for y in range(self.altura):
                c = 2 * self.get_pixel(x, y) - borrada.get_pixel(x, y)
                resultado.set_pixel(x, y, c)
        resultado = resultado.aplicar_por_pixel(lambda c: max(min(round(c), 255), 0))
        return resultado

    def bordas(self):
        kernel_x = [[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]]  # Kernel Kx
        kernel_y = [[-1, -2, -1], [0, 0, 0], [1, 2, 1]]  # Kernel Ky
        gradiente_x = self.correlacionar(kernel_x)  # Calcula o gradiente horizontal
        gradiente_y = self.correlacionar(kernel_y)  # Calcula o gradiente vertical
        resultado = Imagem.nova(self.largura, self.altura)
        for x in range(self.largura):
            for y in range(self.altura):
                gx = gradiente_x.get_pixel(x, y)
                gy = gradiente_y.get_pixel(x, y)
                magnitude = math.sqrt(gx ** 2 + gy ** 2)  # Calcula a magnitude do gradiente
                magnitude = max(min(round(magnitude), 255), 0) # Arredonda e garante que o valor esteja no intervalo [0, 255]
                resultado.set_pixel(x, y, magnitude)
        return resultado

    # Abaixo deste ponto estão utilitários para carregar, salvar e mostrar
    # as imagens, bem como para a realização de testes.

    def __eq__(self, other):
        return all(getattr(self, i) == getattr(other, i)
                   for i in ('altura', 'largura', 'pixels'))

    def __repr__(self):
        return "Imagem(%s, %s, %s)" % (self.largura, self.altura, self.pixels)

    @classmethod
    def carregar(cls, nome_arquivo):
        """
        Carrega uma imagem do arquivo fornecido e retorna uma instância dessa
        classe representando essa imagem. Também realiza a conversão para tons
        de cinza.

        Invocado como, por exemplo:
           i = Imagem.carregar('test_images/cat.png')
        """
        with open(nome_arquivo, 'rb') as guia_para_imagem:
            img = PILImage.open(guia_para_imagem)
            img_data = img.getdata()
            if img.mode.startswith('RGB'):
                pixels = [round(.299 * p[0] + .587 * p[1] + .114 * p[2]) for p in img_data]
            elif img.mode == 'LA':
                pixels = [p[0] for p in img_data]
            elif img.mode == 'L':
                pixels = list(img_data)
            else:
                raise ValueError('Modo de imagem não suportado: %r' % img.mode)
            l, a = img.size
            return cls(l, a, pixels)

    @classmethod
    def nova(cls, largura, altura):
        """
        Cria imagens em branco (tudo 0) com a altura e largura fornecidas.

        Invocado como, por exemplo:
            i = Imagem.nova(640, 480)
        """
        return cls(largura, altura, [0 for i in range(largura * altura)])

    def salvar(self, nome_arquivo, modo='PNG'):
        """
        Salva a imagem fornecida no disco ou em um objeto semelhante a um arquivo.
        Se o nome_arquivo for fornecido como uma string, o tipo de arquivo será
        inferido a partir do nome fornecido. Se nome_arquivo for fornecido como
        um objeto semelhante a um arquivo, o tipo de arquivo será determinado
        pelo parâmetro 'modo'.
        """
        saida = PILImage.new(mode='L', size=(self.largura, self.altura))
        saida.putdata(self.pixels)
        if isinstance(nome_arquivo, str):
            saida.save(nome_arquivo)
        else:
            saida.save(nome_arquivo, modo)
        saida.close()

    def gif_data(self):
        """
        Retorna uma string codificada em base 64, contendo a imagem
        fornecida, como uma imagem GIF.

        Função utilitária para tornar show_image um pouco mais limpo.
        """
        buffer = BytesIO()
        self.salvar(buffer, modo='GIF')
        return base64.b64encode(buffer.getvalue())

    def mostrar(self):
        """
        Mostra uma imagem em uma nova janela Tk.
        """
        global WINDOWS_OPENED
        if tk_root is None:
            # Se Tk não foi inicializado corretamente, não faz mais nada.
            return
        WINDOWS_OPENED = True
        toplevel = tkinter.Toplevel()
        # O highlightthickness=0 é um hack para evitar que o redimensionamento da janela
        # dispare outro evento de redimensionamento (causando um loop infinito de
        # redimensionamento). Para maiores informações, ver:
        # https://stackoverflow.com/questions/22838255/tkinter-canvas-resizing-automatically
        tela = tkinter.Canvas(toplevel, height=self.altura,
                              width=self.largura, highlightthickness=0)
        tela.pack()
        tela.img = tkinter.PhotoImage(data=self.gif_data())
        tela.create_image(0, 0, image=tela.img, anchor=tkinter.NW)

        def ao_redimensionar(event):
            # Lida com o redimensionamento da imagem quando a tela é redimensionada.
            # O procedimento é:
            #  * converter para uma imagem PIL
            #  * redimensionar aquela imagem
            #  * obter os dados GIF codificados em base 64 (base64-encoded GIF data)
            #    a partir da imagem redimensionada
            #  * colocar isso em um label tkinter
            #  * mostrar a imagem na tela
            nova_imagem = PILImage.new(mode='L', size=(self.largura, self.altura))
            nova_imagem.putdata(self.pixels)
            nova_imagem = nova_imagem.resize((event.largura, event.altura), PILImage.NEAREST)
            buffer = BytesIO()
            nova_imagem.save(buffer, 'GIF')
            tela.img = tkinter.PhotoImage(data=base64.b64encode(buffer.getvalue()))
            tela.configure(height=event.altura, width=event.largura)
            tela.create_image(0, 0, image=tela.img, anchor=tkinter.NW)

        # Por fim, faz o bind da função para que ela seja chamada quando a tela
        # for redimensionada:
        tela.bind('<Configure>', ao_redimensionar)
        toplevel.bind('<Configure>', lambda e: tela.configure(height=e.altura, width=e.largura))

        # Quando a tela é fechada, o programa deve parar
        toplevel.protocol('WM_DELETE_WINDOW', tk_root.destroy)


# Não altere o comentário abaixo:
# noinspection PyBroadException
try:
    tk_root = tkinter.Tk()
    tk_root.withdraw()
    tcl = tkinter.Tcl()


    def refaz_apos():
        tcl.after(500, refaz_apos)


    tcl.after(500, refaz_apos)
except:
    tk_root = None

WINDOWS_OPENED = False

if __name__ == '__main__':
    # O código neste bloco só será executado quando você executar
    # explicitamente seu script e não quando os testes estiverem
    # sendo executados. Este é um bom lugar para gerar imagens, etc.


    imagem = Imagem.carregar('test_images/construct.png')
    bordas = imagem.bordas()
    bordas.mostrar("test_results/construct.png")

    pass

    # O código a seguir fará com que as janelas de Imagem.mostrar
    # sejam exibidas corretamente, quer estejamos executando
    # interativamente ou não:
    if WINDOWS_OPENED and not sys.flags.interactive:
        tk_root.mainloop()
