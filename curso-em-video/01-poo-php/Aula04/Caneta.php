<?php
class Caneta {
  private $modelo;
  private $cor;
  private $ponta;
  private $tampada;
  
  function __construct($modelo, $cor, $ponta) {
    $this->modelo = $modelo;
    $this->cor = $cor;
    $this->ponta = $ponta;
    $this->setTampada(true);
  }

  function getModelo() {
    return $this->modelo;
  }

  function getCor() {
    return $this->cor;
  }

  function getPonta() {
    return $this->ponta;
  }

  function getTampada() {
    return $this->tampada;
  }

  function setModelo($modelo): void {
    $this->modelo = $modelo;
  }

  function setCor($cor): void {
    $this->cor = $cor;
  }

  function setPonta($ponta): void {
    $this->ponta = $ponta;
  }

  function setTampada($tampada): void {
    $this->tampada = $tampada;
  }
}
