<?php
class ContaBancaria {
  public $numConta;
  protected $tipo;  
  private $dono;
  private $saldo;
  private $status;
  
  function __construct($numConta, $tipo, $dono) {
    $this->numConta = $numConta;
    $this->setTipo($tipo);
    $this->dono = $dono;
    $this->saldo = 0;
    $this->setStatus(false);
    $this->abrirConta($this->status);
  }

  function getNumConta() {
    return $this->numConta;
  }

  function getTipo() {
    return $this->tipo;
  }

  function getDono() {
    return $this->dono;
  }

  function getSaldo() {
    return $this->saldo;
  }

  function getStatus() {
    return $this->status;
  }

  function setNumConta($numConta): void {
    $this->numConta = $numConta;
  }

  function setTipo($tipo): void {
    $this->tipo = $tipo;
  }

  function setDono($dono): void {
    $this->dono = $dono;
  }

  function setSaldo($saldo): void {
    $this->saldo = $saldo;
  }

  function setStatus($status): void {
    $this->status = $status;
  }
  
  public function abrirConta($status) {
    $status = true;
    
    if($this->tipo == "cc") {
      $this->tipo = "Conta corrente";
      $this->saldo += 50;
    }
    elseif($this->tipo == "cp") {
      $this->tipo = "Conta poupança";
      $this->saldo += 150;
    } 
    
    $this->status = $status;
  }
  
  public function fecharConta() {
    echo "\n--------------------------------\n\n" . 
        $this->tipo . " nº " . $this->numConta . "\nOlá, " . 
        $this->dono . "!\n\nSaldo: R$" . $this->saldo . 
        "\nOperação: Fechar conta";
    
    if($this->saldo > 0) {
      echo "\n\nOperação não efetuada!" .
          "\nNão é possível encerrar a conta se existir saldo!\n";
      $status = true;
    }
    elseif($this->saldo < 0) {
      echo "\n\nOperação não efetuada!" .
          "\nNão é possível encerrar a conta se existir débito!\n";
      $status = true;
    }
    else {
      echo "\n\nConta encerrada com sucesso!\n";
      $status = false;
    }
    
    $this->status = $status; 
  }
  
  public function depositar($quantia) {
    echo "\n--------------------------------\n\n" . 
        $this->tipo . " nº " . $this->numConta . "\nOlá, " . 
        $this->dono . "!\n\nSaldo: R$" . $this->saldo . 
        "\nOperação: Depositar R$" . $quantia;

    if($quantia == 0) {
       echo "\n\nDepósito não efetuado! " .
        "\nValor do depósito não pode ser R$0!\n";
    }
    elseif($quantia < 0) {
      echo "\n\nDepósito não efetuado! " .
        "\nValor do depósito não pode ser negativo!\n";
    }
    else {
     $this->saldo += $quantia;
      echo "\n\nDepósito efetuado com sucesso!";
    }    
    echo "\nSaldo atual: R$" . $this->saldo . "\n";
  }
   
  public function sacar($quantia) {
    echo "\n--------------------------------\n\n" .
        $this->tipo . " nº " . $this->numConta . "\nOlá, " . 
        $this->dono . "!\n\nSaldo: R$" . $this->saldo .
        "\nOperação: Sacar R$" . $quantia;
    
    if($quantia == 0) {
      echo "\n\nSaque não efetuado! " .
          "\nValor do saque não pode ser R$0!\n";
    }
    elseif($quantia < 0) {
      echo "\n\nSaque não efetuado! " .
          "\nValor do saque não pode ser negativo!\n";
    }
    elseif($quantia > $this->saldo) {
      echo "\n\nSaque não efetuado! " .
          "\nValor do saque não pode ser maior do que o do saldo!\n";
    }    
    else {
     $this->saldo -= $quantia;
      echo "\n\nSaque efetuado com sucesso!";
    }
    echo "\nSaldo atual: R$" . $this->saldo . "\n";
  }
  
  public function pagarMensal() {
    echo "\n--------------------------------\n\n" . 
        $this->tipo . " nº " . $this->numConta . "\nOlá, " . 
        $this->dono . "!\n\nSaldo: R$" . $this->saldo . 
        "\nOperação: Pagar mensalidade";
    
    if($this->tipo = "Conta corrente") {
      $mensalidade = 12;      
    }
    elseif($this->tipo = "Conta poupança") {
      $mensalidade = 20;
    }
    
    $this->saldo -= $mensalidade;
    echo "\nMensalidade: R$" . $mensalidade .
        "\n\nOperação realizada com sucesso!\nSaldo atual: R$" . $this->saldo;
  }
}
