# descobrir quais numeros do array somados dão 10
def findPair(nums, target):

    for i in range(len(nums) - 1):


        for j in range(i + 1, len(nums)):


            if nums[i] + nums[j] == target:
                print('Pair found', (nums[i], nums[j]))
                return


    print('Pair not found')


if __name__ == '__main__':
    array = [3,5,-4,8,11,1,-1,6]
    targetSum = 10

    findPair(array, targetSum)

