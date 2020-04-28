def find_files(filesList):
    
    def listFilesInRepo(repoName, globalUser, token, directory):
    # function that returns the github objects for the content
    # of a directory inside a github repo
        from github import Github
        g = Github(token)
        fullRepoName = globalUser + "/" + repoName
        print(fullRepoName)
        try:
            repo = g.get_repo(fullRepoName)
            contents = repo.get_contents(directory)
            size = len(contents)
            result = []
            for bucle in range(size):
                fileName = contents[bucle].raw_data["name"]
                print(fileName)
                result.append(fileName)
            return result
        except:
            print ("wrong repo")
            contents = False
            return (contents)
    
    
    token = "1a7fdb0af7573fdc17f0d9cabd2c6a1f05765abe"
    #globalUser = "smart-data-models"
    globalUser = "albertoabellagarcia"
    directory = "/"
    repoName = "test2"
    listedFiles = listFilesInRepo(repoName, globalUser, token, directory)
    foundFiles = True
    for file in filesList:
        foundFiles = foundFiles * (file in listedFiles)
    return foundFiles

def test_find_files():
    filesList = ["recurso.csv"]
    assert find_files(filesList)
