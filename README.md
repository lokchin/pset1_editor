## Questão 1

O output esperado seria [255 - o número no array], no caso.
[226, 166, 119, 55]
O espectro de 4 pixels invertido, como está acima, está escurecendo.

## Questão 2

    imagem = Imagem.carregar("test_images/bluegill.png")
    imagem_invertida = imagem.invertida()
    imagem_invertida.salvar("test_results/bluegill_invertida.png")

![bluegill_invertida.png](https://github.com/lokchin/ling_prog_pset1/blob/main/test_results/bluegill_invertida.png)

## Questão 3

|     |     |     | 
| --- | --- | --- |
| 0.00 | -0.07 | 0.00 | 
| -0.45 | 1.20 | -0.25 |
| 0.00 | -0.12 | 0.00 |

###### X

|     |     |     |
|---| --- | --- |
| 80 | 53 | 99 |
| 129 | 127 | 148 |
| 175 | 174 | 193 |

#### 👇

|   |     |     |                   
|---|-----|-----|                  
| 80 x 0.00 +| 53 x (-0.07) + | 99 x 0.00 + |            
| 129 x (-0.45) +| 127 x 1.20 + | 148 x (-0.25) + |           
| 175 x 0.00 + | 174 x (-0.12) + | 193 x 0.00 |

###### = 32,76
<br>

## Questão 4

```
    imagem = Imagem.carregar('test_images/pigbird.png')
    kernel = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
    resultado = imagem.correlacionar(kernel)
    resultado.salvar('test_results/pigbird.png')
```

   ![pigbird.png](https://github.com/lokchin/ling_prog_pset1/blob/main/test_results/pigbird.png)

## Questão 5

Utilizando como exemplo o kernel:
 
    [[0, -1, 0],
    [-1, 5, -1],
    [0, -1, 0]]

Adicionado à formula:
```
Sx,y = round(2Ix,y − Bx,y)
```

O cálculo seria:

```
Sx,y = round(
    2 * ((Ix-1, y-1)*0 + (Ix, y-1)*(-1) + (Ix+1, y-1)*0 +
         (Ix-1, y)*(-1) + (Ix,y)*5 + (Ix+1, y)*(-1) +
         (Ix-1, y+1)*0 + (Ix, y+1)*(-1) + (Ix+1, y+1)(*0)) - Bx,y
         )

```
Chamada:
```
imagem = Imagem.carregar('test_images/python.png')
imagem_nitida = imagem.focada(11)
imagem_nitida.salvar('test_results/python.png')
```

![python.png](https://github.com/lokchin/ling_prog_pset1/blob/main/test_results/python.png)

## Questão 6

O kernel Kx calcula o gradiente na horizontal, já o Ky, na vertical. Eles fazem uma operação de convolução e destacam a diferença de intensidade entre os pixels adjacentes referentes aos seus eixos (x, y). A combinação de Kx e Ky de valores permite a detecção de bordas na imagem.

```
    imagem = Imagem.carregar('test_images/construct.png')
    bordas = imagem.bordas()
    bordas.salvar("test_results/construct.png")
```
![construct.png](https://github.com/lokchin/ling_prog_pset1/blob/main/test_results/construct.png)

## Demonstrações extras

![imagem_gato_borrada.png](https://github.com/lokchin/ling_prog_pset1/blob/main/test_results/imagem_gato_borrada.png)

