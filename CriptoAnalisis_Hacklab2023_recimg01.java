import java.util.*;
import java.io.*;

/*
Genera una matriz de bits de paridad para un archivo.
Cada fila de la matriz tendrÃ¡ 16 bits (2 bytes) y la cantidad de filas dependerÃ¡
del tamaÃ±o del archivo.
*/

public class BitParidad{
    public static void main(String args[]) throws IOException, FileNotFoundException{
        File archivo = new File(args[0]);
        FileInputStream fis = new FileInputStream(archivo);

        //File archivoSalida = new File("bitsParidad");
        //FileOutputStream fos = new FileOutputStream(archivoSalida);
        List<BitParidadPaquete> bpPaquetes = new LinkedList<>();

        int b;
        int bytesLeidos = 0;
        int totalBytesLeidos = 0;
        byte paquete[] = new byte[10];
        while((b = fis.read()) != -1){
            paquete[bytesLeidos] = (byte) b;
            bytesLeidos++;
            if(bytesLeidos == 10){
                totalBytesLeidos += bytesLeidos;
                
                // Paquete leÃ­do.
                BitParidadPaquete bpPaquete = new BitParidadPaquete();
                for(int i = 0; i < paquete.length; i += 2){
                    int bp = bitParidad(paquete[i], paquete[i + 1]);
                    bpPaquete.bpFilas[i / 2] = bp;
                    
                    int palabraAnalizando = paquete[i];
                    int mascara = 1;
                    for(int j = 0; j < 16; j++){
                        if(j == 8){
                            palabraAnalizando = paquete[i + 1];
                            mascara = 1;
                        }
                        if((palabraAnalizando & mascara) == mascara){
                            bpPaquete.bpColumnas[16 - j - 1] = (bpPaquete.bpColumnas[16 - j - 1] += 1) % 2;
                        }
                        mascara <<= 1;
                    }
                }
                bpPaquetes.add(bpPaquete);
                bytesLeidos = 0;
            }
        }
        
        fis.close();
        Iterator<BitParidadPaquete> it = bpPaquetes.iterator();
        while(it.hasNext()){
            System.out.print(it.next());
        }
        //fos.close();
    }

    private static int bitParidad(int b1, int b2){
        int n1 = Integer.bitCount(b1);
        int n2 = Integer.bitCount(b2);
        int r = 1;
        if((n1 + n2) % 2 == 0){
            r = 0;
        }
        return r;
    }
    
    static class BitParidadPaquete{
        int bpFilas[];
        int bpColumnas[];
        public BitParidadPaquete(){
            this.bpFilas = new int[5];
            this.bpColumnas = new int[16];
        }
        
        @Override
        public String toString(){
            StringBuilder sb = new StringBuilder();
            for(int i = 0; i < bpFilas.length; i++){
                sb.append(bpFilas[i]);
            }
            sb.append(" ");
            for(int i = 0; i < bpColumnas.length; i++){
                sb.append(bpColumnas[i]);
            }
            sb.append("\n");
            return sb.toString();
        }
    }
}
