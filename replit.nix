{ pkgs }: {
	deps = [
		pkgs.run
  pkgs.nodejs-16_x
  pkgs.jq.bin
  pkgs.dotnet-sdk
    pkgs.omnisharp-roslyn
	];
}