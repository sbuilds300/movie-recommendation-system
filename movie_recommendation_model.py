{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOWyDOX1nmZZ2Nkz3GPi1uV",
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
        "<a href=\"https://colab.research.google.com/github/sbuilds300/movie-recommendation-system/blob/main/movie_recommendation_model.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 6,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "gBq6QLVSAH5K",
        "outputId": "c9d3c732-8523-4cc6-f34a-732585e5a8df",
        "collapsed": true
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[[1.         0.42289003 0.93895296 0.26519742]\n",
            " [0.42289003 1.         0.41573971 0.98130676]\n",
            " [0.93895296 0.41573971 1.         0.30261377]\n",
            " [0.26519742 0.98130676 0.30261377 1.        ]]\n",
            "\n",
            "Because you liked Avengers,you should watch :Deadpool , Titanic\n"
          ]
        }
      ],
      "source": [
        "import numpy as np\n",
        "from sklearn.metrics.pairwise import cosine_similarity\n",
        "#Define the Dataset\n",
        "# Features could represent [Action, Romance, Comedy] ratings\n",
        "movies={\n",
        "    \"Avengers\":[5,1,3],\n",
        "    \"Titanic\": [1, 5, 1],\n",
        "    \"Deadpool\": [4, 1, 5],\n",
        "    \"The Notebook\": [0, 5, 1]\n",
        "}\n",
        "# 2. Data Preprocessing\n",
        "#convert to matrix\n",
        "\n",
        "movies_name=list(movies.keys())\n",
        "movies_vector=np.array(list(movies.values()))\n",
        "\n",
        "#compute similarity matrix\n",
        "# This calculates how mathematically similar each movie vector is to the others\n",
        "\n",
        "similarity_matrix=cosine_similarity(movies_vector)\n",
        "print(similarity_matrix)\n",
        "\n",
        "def recommendation(movie_name):\n",
        "  \"\"\"\n",
        "    Finds the top 2 movies similar to the input movie using\n",
        "    cosine similarity scores.\n",
        "    \"\"\"\n",
        "  # find the index of our movies in the list\n",
        "\n",
        "  index=movies_name.index(movie_name)\n",
        "\n",
        "  #Create a list of (index, similarity_score) pairs for this movie\n",
        "\n",
        "  similarity_score=list(enumerate(similarity_matrix[index]))\n",
        "\n",
        "  #Sort the list by score in descending order (highest similarity first)\n",
        "\n",
        "  similarity_score=sorted(similarity_score,key=lambda x:x[1],reverse=True)\n",
        "\n",
        "  #Grab the second movie (index 1 in the sorted list)\n",
        "    # index 0 is the movie itself!\n",
        "\n",
        "  recommended_movie_index=[i[0] for i in similarity_score[1:3]]\n",
        "\n",
        "  #conversts indices to movies_name\n",
        "\n",
        "  recommended_movie_name=[movies_name[i] for i in recommended_movie_index]\n",
        "\n",
        "  return recommended_movie_name\n",
        "\n",
        "if __name__=='__main__':\n",
        "\n",
        "  target_movie=input(\"Enter the movie name :\")\n",
        "\n",
        "  suggestion = recommendation(target_movie)\n",
        "\n",
        "  print(f\"\\nBecause you liked {target_movie},you should watch :{' , '.join(suggestion)}\")\n",
        "\n"
      ]
    }
  ]
}
