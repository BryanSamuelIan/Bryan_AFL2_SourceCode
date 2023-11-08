#include <iostream>
using namespace std;

// Function to check if the current stream item(key) exists in any of the frames or not
int search(int key, int frame_items[], int frame_occupied) {
    for (int i = 0; i < frame_occupied; i++) {
        if (frame_items[i] == key) {
            return 1; // Hit
        }
    }
    return 0; // Miss
}

void printOuterStructure(int max_frames) {
    cout << "Stream ";
    for (int i = 0; i < max_frames; i++) {
        cout << "Frame" << i + 1 << ' ';
    }
    cout << endl;
}

void printCurrFrames(int item, int frame_items[], int frame_occupied, int max_frames, int hit) {
    cout << item << "\t\t";
    for (int i = 0; i < max_frames; i++) {
        if (i < frame_occupied) {
            cout << frame_items[i] << "\t\t";
        } else {
            cout << "-\t\t";
        }
    }
    if (hit) {
        cout << "Hit" << endl;
    } else {
        cout << "Miss" << endl;
    }
}

// Function to find the frame that will not be used for the longest period of time in the future
int predict(int ref_str[], int frame_items[], int refStrLen, int index, int frame_occupied) {
    int result = -1;
    int farthest = index;
    for (int i = 0; i < frame_occupied; i++) {
        int j;
        for (j = index; j < refStrLen; j++) {
            if (frame_items[i] == ref_str[j]) {
                if (j > farthest) {
                    farthest = j;
                    result = i;
                }
                break;
            }
        }
        // If we find a page that is never referenced in the future, return it immediately as the best
        if (j == refStrLen) {
            return i;
        }
    }
    // If none of the frame items appear in the reference string in the future, then we return the 0th index.Otherwise, we return the result.
    return (result == -1) ? 0 : result;
}

void optimalPage(int ref_str[], int refStrLen, int frame_items[], int max_frames) {
    // Initially, none of the frames are occupied
    int frame_occupied = 0;
    printOuterStructure(max_frames);

    int hits = 0;
    for (int i = 0; i < refStrLen; i++) {
        // If found already in the frame items: HIT
        if (search(ref_str[i], frame_items, frame_occupied)) {
            hits++;
            printCurrFrames(ref_str[i], frame_items, frame_occupied, max_frames, 1); // Print "Hit"
            continue;
        }

        // If not found in frame items: MISS

        // If frames are empty, then the current reference string item in a frame
        if (frame_occupied < max_frames) {
            frame_items[frame_occupied] = ref_str[i];
            frame_occupied++;
            printCurrFrames(ref_str[i], frame_items, frame_occupied, max_frames, 0); // Print "Miss"
        }
        // Else we need to use the optimal algorithm to find the frame index where we need to do replacement for this incoming reference string item
        else {
            int pos = predict(ref_str, frame_items, refStrLen, i + 1, frame_occupied);
            frame_items[pos] = ref_str[i];
            printCurrFrames(ref_str[i], frame_items, frame_occupied, max_frames, 0); // Print "Miss"
        }
    }

    cout << "\nHits: " << hits << endl;
    cout << "Misses: " << refStrLen - hits << endl;
}

int main() {
    // int ref_str[] = {9, 0, 5, 1, 0, 3, 0, 4, 1, 3, 0, 3, 1, 3};
    int ref_str[] = {7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2, 1, 2, 0, 1, 7, 0, 1};
    int refStrLen = sizeof(ref_str) / sizeof(ref_str[0]);
    int max_frames = 3;
    int frame_items[max_frames];

    optimalPage(ref_str, refStrLen, frame_items, max_frames);
    return 0;
}