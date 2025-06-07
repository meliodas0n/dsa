# shell.nix
{ pkgs ? import <nixpkgs> {} }:
pkgs.mkShell {
  buildInputs = with pkgs; [
    python311Full
    python311Packages.jupyter
    python311Packages.ipykernel
    python311Packages.numpy
    python311Packages.pandas
  ];
}

