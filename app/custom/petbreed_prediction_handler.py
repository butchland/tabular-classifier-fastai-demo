# custom prediction handler module

threshold = 0.95
threshold2 = 0.5
# the prediction handler should always have at least 3 parameters
# the prediction (which is the predicted class of the image), 
# the index position of the predicted class (based on the model.classes),
# and the probabilities array for each class -- it should be highest for the predicted class
# the method should return either a string or a json object. 
# the returned json object is handled in the client.js for the default web app included in the template
def handle_prediction(prediction, index, probabilities):
    highest_probability = float(probabilities[int(index)])
    if (highest_probability < threshold2) : 
        result = "Totally can't guess"
    elif (highest_probability < threshold) :
        label = "Don't know but it might be a/an " + str(prediction)
        result = label + ' with a probability of  %.2f percent' % (highest_probability * 100)
    else:
        label = 'Its probably a/an ' + str(prediction)
        result = label + ' with a probability of  %.2f percent' % (highest_probability * 100)
    return result


__all__ = ['handle_prediction']