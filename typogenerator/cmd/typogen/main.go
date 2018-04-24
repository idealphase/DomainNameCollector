package main

import (
	//"fmt"
	"log"
    "strconv"
	"os"
    "strings"
    // self added to read domain name file
    "bufio"

	"golang.org/x/net/idna"
    "time"

	"github.com/Zenithar/typogenerator"
	"github.com/Zenithar/typogenerator/mapping"
	"github.com/Zenithar/typogenerator/strategy"

	"github.com/hduplooy/gocsv"
	"github.com/namsral/flag"
)

var (
	input           = flag.String("s", "zenithar", "Defines string to alternate")
	permutationOnly = flag.Bool("p", false, "Display permutted domain only")
)

func init() {
	flag.Parse()
}

func FloatToString(input_num float64) string {
    // to convert a float number to a string
        return strconv.FormatFloat(input_num, 'f', 6, 64)
}


func main() {
	all := []strategy.Strategy{
		strategy.Addition,
		strategy.BitSquatting,
		strategy.Homoglyph,
		strategy.Omission,
		strategy.Repetition,
		strategy.Transposition,
		strategy.Prefix,
		strategy.Hyphenation,
		strategy.SubDomain,
		strategy.VowelSwap,
		strategy.Replace(mapping.English),
		strategy.DoubleHit(mapping.English),
	}

    file, err := os.Open("./merge_complete.txt")
    if err != nil {
        log.Fatal("Unable to open merge_complete.txt")
    }
    defer file.Close()

    scanner :=  bufio.NewScanner(file)
    for scanner.Scan() {
        //fmt.Println(scanner.Text())
        results, err := typogenerator.Fuzz(strings.TrimSuffix(scanner.Text(),"\n"), all...)
        if err !=nil {
            log.Fatal("Unable to generate domain")
        }
        writer := gocsv.NewWriter(os.Stdout)
        writer.QuoteFields = true
        defer writer.Flush()
        
        //fmt.Println(results[0])
        //fmt.Println(results[1])
        
        t1 := time.Now()
        for _, r := range results {
            for _, p := range r.Permutations {
                puny, _ := idna.ToASCII(p)    
                //writer.Write([]string{r.StrategyName, puny})
                writer.Write([]string{r.StrategyName, r.Domain,puny})
            }
            //fmt.Println(strings.Replace(r.StrategyName," ","_",2),r.Domain,r.Permutations)
        }
        t2 := time.Now()
        diff := t2.Sub(t1)
        writer.Write([]string{strconv.FormatInt(diff.Nanoseconds(),10)})
    }

    /*
	results, err := typogenerator.Fuzz(*input, all...)
	if err != nil {
		log.Fatal("Unable to generate domains.")
	}

	if !*permutationOnly {
		writer := gocsv.NewWriter(os.Stdout)
		writer.QuoteFields = true
		defer writer.Flush()

		// Write headers
		//writer.Write([]string{"strategy", "domain", "permunation", "idna"})

		for _, r := range results {
			for _, p := range r.Permutations {
				puny, _ := idna.ToASCII(p)
				writer.Write([]string{r.StrategyName., r.Domain, p, puny})
			}
		}
	} else {
		for _, r := range results {
			for _, p := range r.Permutations {
				fmt.Println(p)
			}
		}
	}*/

}
