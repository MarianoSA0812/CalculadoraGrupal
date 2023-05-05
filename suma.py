{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "mount_file_id": "1fJOU5YPmhNFkk8tMCokYtV6J4J_YKm4i",
      "authorship_tag": "ABX9TyMoDVCAjHf0KwPjtcCitD0f",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/MarianoSA0812/CalculadoraGrupal/blob/Suma/suma.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 2,
      "metadata": {
        "id": "yewHJJ0DXm8f"
      },
      "outputs": [],
      "source": [
        "!git config --global user.email \"leanx777@gmail.com\"\n",
        "!git config --global user.name \"LeandroAsis\""
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "%cd /content/CalculadoraGrupal"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "f0YudfmlX99a",
        "outputId": "b8080330-ba06-45a6-83f9-c122a146751b"
      },
      "execution_count": 11,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "/content/CalculadoraGrupal\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!git clone https://github.com/MarianoSA0812/CalculadoraGrupal.git"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "UOZRjUavYN0q",
        "outputId": "1909711d-cfde-4fa2-900c-b7a636ce92c9"
      },
      "execution_count": 4,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Cloning into 'CalculadoraGrupal'...\n",
            "remote: Enumerating objects: 28, done.\u001b[K\n",
            "remote: Counting objects: 100% (28/28), done.\u001b[K\n",
            "remote: Compressing objects: 100% (23/23), done.\u001b[K\n",
            "remote: Total 28 (delta 9), reused 0 (delta 0), pack-reused 0\u001b[K\n",
            "Unpacking objects: 100% (28/28), 5.02 KiB | 733.00 KiB/s, done.\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!ls"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "W8ozWyXJYT6S",
        "outputId": "774842f2-847b-4e97-f723-367e86362684"
      },
      "execution_count": 13,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "README.md\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!git status"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "XvHeM7m9Y2RC",
        "outputId": "a1271f0b-de06-4690-ad1f-411a2c666070"
      },
      "execution_count": 17,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "On branch main\n",
            "Your branch is up to date with 'origin/main'.\n",
            "\n",
            "Changes to be committed:\n",
            "  (use \"git restore --staged <file>...\" to unstage)\n",
            "\t\u001b[32mnew file:   suma.py\u001b[m\n",
            "\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!git add suma.py"
      ],
      "metadata": {
        "id": "w425MesaY53j"
      },
      "execution_count": 16,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "!git commit -m \"Leandro Asis: realice el codigo de la suma el dia 04/05/2023\""
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "HigXK_cGZyAr",
        "outputId": "72b88c5b-1d5b-41b1-d2d9-da5e036db63a"
      },
      "execution_count": 18,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[main 85246b6] Leandro Asis: realice el codigo de la suma el dia 04/05/2023\n",
            " 1 file changed, 3 insertions(+)\n",
            " create mode 100644 suma.py\n"
          ]
        }
      ]
    }
  ]
}