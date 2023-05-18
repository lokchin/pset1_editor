## Questão 1

O output esperado seria [256 - o número no array], no caso.
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

## Questão 4

