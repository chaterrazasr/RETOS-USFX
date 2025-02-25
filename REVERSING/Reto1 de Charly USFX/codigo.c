#include <stdio.h>
#include <string.h>

int es_color_valido(char *color) {
    char *colores_validos[] = {"rojo", "verde", "azul", "negro", "blanco", "amarillo", "rosado", "naranja", "morado", "marrón"};
    int num_colores = 10;
    for (int i = 0; i < num_colores; i++) {
        if (strcmp(color, colores_validos[i]) == 0) {
            return 1;
        }
    }
    return 0;
}

void desencriptar_flag(char *encriptado, int desplazamiento) {
    char flag[100];
    int len = strlen(encriptado);
    for (int i = 0; i < len; i++) {
        flag[i] = ((encriptado[i] - 'a' - desplazamiento + 26) % 26) + 'a';
    }
    flag[len] = '\0';
    printf("FLAG: %s\n", flag);
}

int main() {
    char colores[4][10];
    char *nombres[] = {"Liam", "Olivia", "Noah", "Sophia"};
    char *colores_correctos[] = {"rojo", "verde", "azul", "negro"};
    char flag_encriptada[] = "edqghudghfroruhv";
    int desplazamiento = 3;
    int correctos = 1;

    printf("El Reto de los Artistas: Un grupo de amigos artistas —Liam, Olivia, Noah y Sophia— \ntiene un juego especial para aquellos que deseen unirse a su círculo. \nTu objetivo es descubrir sus colores favoritos, cada uno único y cuidadosamente elegido.\n\n");

    for (int i = 0; i < 4; i++) {
        while (1) {
            printf("Por favor, elige el color favorito de %s: ", nombres[i]);
            scanf("%9s", colores[i]);
            if (!es_color_valido(colores[i])) {
                printf("¡Color inválido!\n");
            } else {
                int repetido = 0;
                for (int j = 0; j < i; j++) {
                    if (strcmp(colores[i], colores[j]) == 0) {
                        printf("¡Esa opción ya fue elegida!\n");
                        repetido = 1;
                        break;
                    }
                }
                if (!repetido) break;
            }
        }
        if (strcmp(colores[i], colores_correctos[i]) != 0) {
            correctos = 0;
        }
    }

    if (correctos) {
        printf("¡Felicidades! Has adivinado todos los colores favoritos correctamente y ganado el reto.\n");
        desencriptar_flag(flag_encriptada, desplazamiento);
    } else {
        printf("Algunos colores están incorrectos. Por favor, inténtalo de nuevo.\n");
    }

    return 0;
}
