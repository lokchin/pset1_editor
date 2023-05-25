## Questão 1

O output esperado seria [255 - o número no array], no caso.
[227, 167, 120, 56]
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
    imagem = PILImage.open("test_images/pigbird.png")
    largura, altura = imagem.size
    pixels = list(imagem.getdata())
    imagem_obj = Imagem(largura, altura, pixels)
    kernel = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]]
    resultado = imagem_obj.correlacionar(kernel)
    nova_imagem = PILImage.new("RGB", (largura, altura))
    nova_imagem.putdata(resultado.pixels)
    nova_imagem.save("test_results/pigbird.png")
```

   ![pigbird.png](https://github.com/lokchin/ling_prog_pset1/blob/main/test_results/pigbird.png)

```
    imagem = Imagem.carregar("test_images/cat.png")
    imagem_borrada = imagem.borrada(5)
    imagem_borrada.salvar("test_results/imagem_gato_borrada.png")
```

   ![imagem_gato_borrada.png](https://github.com/lokchin/ling_prog_pset1/blob/main/test_results/imagem_gato_borrada.png)
