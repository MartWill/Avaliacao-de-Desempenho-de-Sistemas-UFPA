using System;
using System.IO;
using System.Text;
using System.Diagnostics;

namespace CSVReader
{
  class Program
  {
    static void Main(string[] args)
    {
      var tempoDeExecucao = new Stopwatch();
      tempoDeExecucao.Start();
      /** TABELA 1 **/
      string[] matriz01 = File.ReadAllLines("500_01.csv", Encoding.Default);
      int[][] tabela1 = new int[matriz01.Length][];
      int auxY = 0;
      foreach (string linha01 in matriz01)
      {
        string[] coluna01 = linha01.Split(',');
        int[] linha = new int[coluna01.Length];

        for(int i = 0; i< linha.Length;i++){
          linha[i] = Convert.ToInt32(coluna01[i]);
        }

        tabela1[auxY] = linha; 
        auxY += 1;
      }

      /** TABELA 2 **/
      string[] matriz02 = File.ReadAllLines("500_02.csv", Encoding.Default);
      int[][] tabela2 = new int[matriz02.Length][];
      auxY = 0;
      foreach (string linha01 in matriz02)
      {
        string[] coluna01 = linha01.Split(',');
        int[] linha = new int[coluna01.Length];

        for(int i = 0; i< linha.Length;i++){
          linha[i] = Convert.ToInt32(coluna01[i]);
        }

        tabela2[auxY] = linha; 
        auxY += 1;
      }

      long[][] tabela3 = new long[tabela1.Length][];
      //tabela3 = tabela2;

      for (int coluna = 0; coluna < tabela1.Length; coluna++){
            tabela3[coluna] = new long[tabela1.Length];
      }
      
      /** MULTIPLICAÇÃO **/
      for (int linha = 0; linha < tabela1.Length; linha++){
          for (int coluna = 0; coluna < tabela2[0].Length; coluna++){
              for (int i = 0; i < tabela1[0].Length; i++)  
              {
                  tabela3[linha][coluna] += (long) tabela1[linha][i] * tabela2[i][coluna];
              }
          }
      }

      Stream saida = File.Open("tabela3.csv", FileMode.Create);
      StreamWriter escritor = new StreamWriter(saida);

      for (int linha = 0; linha < tabela3.Length; linha++){
        for (int coluna = 0; coluna < tabela3.Length; coluna++){
             escritor.Write(tabela3[linha][coluna]);
            if(coluna != tabela3[0].Length -1) escritor.Write(',');             
        }
        escritor.WriteLine("");
      }

      Console.WriteLine("FEITO");
      escritor.Close();
      saida.Close();

      // SALVA O TEMPO DE EXECUÇÃO
      tempoDeExecucao.Stop();

      string text = File.ReadAllText("Log.txt"); 
      Stream tempoDecorrido = File.Open("Log.txt", FileMode.Create);
      StreamWriter tempo = new StreamWriter(tempoDecorrido);

      if (text == "")
        tempo.WriteLine("Tempo passado: " + tempoDeExecucao.Elapsed);

      if(text != "")
        tempo.WriteLine(text + "Tempo passado: " + tempoDeExecucao.Elapsed);

      tempo.Close();
      tempoDecorrido.Close();
    } 
  }
}
