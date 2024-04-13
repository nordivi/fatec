
import java.util.logging.Level;
import java.util.logging.Logger;



public class Principal {

    
    public static void main(String[] args) throws InterruptedException {
        System.out.println("Hello World");
        
        System.out.println("Inicializando 1ª Thread");
        Thread.sleep(1000);
        System.out.println("Finalizando 1ª Thread");
        
        System.out.println("Inicializando 2ª Thread");
        Thread.sleep(1000);
        System.out.println("Finalizando 2ª Thread");
        
        System.out.println("Inicializando 3ª Thread");
        Thread.sleep(1000);
        System.out.println("Finalizando 3ª Thread");
        System.out.println("-------- INICIALIZANDO THREADS ---------");
        new Thread(() -> {
            
            System.out.println("1ª Thread - Init");
            try {
                Thread.sleep(1000);
            } catch (InterruptedException ex) {
                Logger.getLogger(Principal.class.getName()).log(Level.SEVERE, null, ex);
            }
            System.out.println("1ª Thread - Final");
            }).start();
        new Thread(() -> {
            System.out.println("2ª Thread - Init");
            try {
                Thread.sleep(1000);
            } catch (InterruptedException ex) {
                Logger.getLogger(Principal.class.getName()).log(Level.SEVERE, null, ex);
            }
            System.out.println("2ª Thread - Final");
            }).start();
        
        new Thread(() -> {
            System.out.println("3ª Thread - Init");
            try {
                Thread.sleep(1000);
            } catch (InterruptedException ex) {
                Logger.getLogger(Principal.class.getName()).log(Level.SEVERE, null, ex);
            }
            System.out.println("3ª Thread - Final");
            }).start();
        
  
    }
    
}
